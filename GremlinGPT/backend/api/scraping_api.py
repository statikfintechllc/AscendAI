#!/usr/bin/env python3

# ─────────────────────────────────────────────────────────────
# ⚠️ GremlinGPT Fair Use Only | Commercial Use Requires License
# Built under the GremlinGPT Dual License v1.0
# © 2025 StatikFintechLLC / AscendAI Project
# Contact: ascend.gremlin@gmail.com
# ─────────────────────────────────────────────────────────────

# GremlinGPT v1.0.3 :: Scraper API & Module Router

from backend.globals import logger

# Core scrapers (import ALL actual scripts from scraper/)
from scraper.scraper_loop import get_dom_html
from scraper.ask_monday_handler import handle as ask_monday_handle
from scraper.web_knowledge_scraper import scrape_web_knowledge
from scraper.dom_navigator import extract_dom_structure
from scraper.source_router import route_scraping_async

import traceback

import asyncio

async def scrape_url(url, method="auto", extra=None):
    """
    Main entry point for dashboard/API. Dispatches to best scraper.
    :param url: target URL (or app for TWS/STT)
    :param method: one of [dom, web, monday, router, auto]
    :param extra: dict, additional args for some scrapers
    :return: dict of scrape results (or error)
    """
    try:
        logger.info(f"[SCRAPER_API] Scrape requested: {url} [{method}]")
        if method == "dom":
            result = await get_dom_html(url)
        elif method == "web":
            result = await scrape_web_knowledge(url)
        elif method == "monday":
            result = ask_monday_handle(url)
        elif method == "router":
            result = await route_scraping_async()
        elif method == "auto":
            # Try DOM first, then Web, then Monday
            try:
                result = await get_dom_html(url)
                if isinstance(result, dict) and result.get("content"):
                    return {"scrape_result": result}
            except Exception:
                pass
            try:
                result = await scrape_web_knowledge(url)
                if isinstance(result, dict) and result.get("content"):
                    return {"scrape_result": result}
            except Exception:
                pass
            if "monday.com" in url:
                try:
                    result = ask_monday_handle(url)
                    if isinstance(result, dict) and result.get("content"):
                        return {"scrape_result": result}
                except Exception:
                    pass
            try:
                result = await route_scraping_async()
                return {"scrape_result": result}
            except Exception:
                return {"error": "All scraping methods failed."}
        else:
            return {"error": f"Unknown scrape method: {method}"}
        return {"scrape_result": result}
    except Exception as e:
        logger.error(f"[SCRAPER_API] Scrape error: {e}\n{traceback.format_exc()}")
        return {"error": str(e), "trace": traceback.format_exc()}


# --- Specialized async/route scraping (source_router, dashboard live) ---


def scrape_router(snapshot=False, periodic=False):
    """
    Run the source_router for full snapshot or periodic live scraping.
    :param snapshot: if True, return full live snapshot (calls get_live_snapshot())
    :param periodic: if True, start/trigger periodic scrape thread
    :return: result dict
    """
    from scraper.source_router import get_live_snapshot, start_scraper_loop

    if snapshot:
        return get_live_snapshot()
    elif periodic:
        start_scraper_loop()
        return {"status": "Periodic scraping loop started"}
    else:
        return {"error": "Specify 'snapshot' or 'periodic' mode."}


# --- Export all major subscrapers for direct API/dashboard use ---

__all__ = [
    "scrape_url",
    "scrape_router",
    "get_dom_html",
    "scrape_web_knowledge",
    "ask_monday_handle",
    "extract_dom_structure",
    "route_scraping_async",
]
