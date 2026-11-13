import flet as ft

def main(page: ft.Page):
    page.title = "简单 Flet App"
    page.add(ft.Text("Hello, Flet!", size=30))

if __name__ == "__main__":
    ft.app(target=main)


# import asyncio
# import logging
# from urllib.parse import quote_plus

# import flet as ft
# from flet_webview import WebView


# LOG_LEVEL = logging.INFO
# logging.basicConfig(format="%(levelname)s %(name)s: %(message)s")
# logging.getLogger("app").setLevel(LOG_LEVEL)
# log = logging.getLogger("app.browser")

# HOME_URL = "https://www.google.com"
# AUTO_PAGE_INTERVAL_SECONDS = 5
# NEXT_PAGE_SCRIPT = r"""(() => {
#   const candidates = Array.from(document.querySelectorAll(
#     'a, button, [role="button"], input[type="button"], input[type="submit"]'
#   ));
#   const labelOf = (el) => [
#     el.innerText,
#     el.textContent,
#     el.value,
#     el.getAttribute('aria-label'),
#     el.title
#   ].filter(Boolean).join(' ').replace(/\s+/g, ' ').trim();
#   const isNext = (label) =>
#     /(下一章|下一页|下一頁|下一话|下一話|next\s+(chapter|page))/i.test(label) ||
#     /^(next|continue)(\s*[›»>→]+)?$/i.test(label);
#   const target = candidates.find((el) => {
#     const label = labelOf(el);
#     const visible = el.getClientRects().length > 0;
#     const disabled = el.disabled || el.getAttribute('aria-disabled') === 'true';
#     const previous = /(上一章|上一页|上一頁|previous|prev)/i.test(label);
#     return visible && !disabled && !previous && isNext(label);
#   });
#   if (target) target.click();
#   return Boolean(target);
# })()"""


# def main(page: ft.Page):
#     page.title = "Flet Browser"
#     address = ft.TextField(
#         value=HOME_URL,
#         hint_text="Search or enter address",
#         expand=True,
#         on_submit=lambda e: navigate(e.control.value),
#     )
#     browser = WebView(url=HOME_URL, expand=True)
#     auto_state = {"running": False}
#     auto_status = ft.Text(
#         "每 5 秒扫描",
#         expand=True,
#         max_lines=1,
#         overflow=ft.TextOverflow.ELLIPSIS,
#     )

#     async def auto_page_loop():
#         while auto_state["running"]:
#             await asyncio.sleep(AUTO_PAGE_INTERVAL_SECONDS)
#             if not auto_state["running"]:
#                 break
#             try:
#                 await browser.run_javascript(NEXT_PAGE_SCRIPT)
#             except Exception:
#                 auto_state["running"] = False
#                 auto_status.value = "网页不支持脚本操作"
#                 auto_button.content = "开始自动翻页"
#                 auto_status.update()
#                 auto_button.update()
#                 log.exception("Automatic page turning failed")
#                 return

#     def toggle_auto_page():
#         auto_state["running"] = not auto_state["running"]
#         if auto_state["running"]:
#             auto_status.value = "已开启 · 再点停止"
#             auto_button.content = "停止自动翻页"
#             asyncio.create_task(auto_page_loop())
#         else:
#             auto_status.value = "已停止"
#             auto_button.content = "开始自动翻页"
#         auto_status.update()
#         auto_button.update()

#     auto_button = ft.Button(content="开始自动翻页", on_click=toggle_auto_page)

#     def normalize_address(value: str) -> str:
#         value = value.strip()
#         if not value:
#             return HOME_URL
#         if value.startswith(("https://", "http://")):
#             return value
#         if " " not in value and ("." in value or value.startswith("localhost")):
#             return f"https://{value}"
#         return f"https://www.google.com/search?q={quote_plus(value)}"

#     def navigate(value: str):
#         target = normalize_address(value)
#         address.value = target
#         browser.url = target
#         browser.update()
#         address.update()
#         log.info("Navigating to %s", target)

#     async def go_back():
#         if await browser.can_go_back():
#             await browser.go_back()

#     async def go_forward():
#         if await browser.can_go_forward():
#             await browser.go_forward()

#     back_button = ft.IconButton(
#         icon=ft.Icons.ARROW_BACK,
#         disabled=True,
#         on_click=go_back,
#     )
#     forward_button = ft.IconButton(
#         icon=ft.Icons.ARROW_FORWARD,
#         disabled=True,
#         on_click=go_forward,
#     )

#     async def sync_navigation():
#         back_button.disabled = not await browser.can_go_back()
#         forward_button.disabled = not await browser.can_go_forward()
#         back_button.update()
#         forward_button.update()

#     async def page_ended(e):
#         current_url = await browser.get_current_url()
#         if current_url:
#             address.value = current_url
#             address.update()
#         await sync_navigation()

#     async def refresh():
#         await browser.reload()

#     async def go_home():
#         navigate(HOME_URL)

#     browser.on_page_ended = page_ended
#     browser.on_url_change = lambda e: sync_address(e.data)

#     def sync_address(value: str):
#         address.value = value
#         address.update()

#     toolbar = ft.Row(
#         controls=[
#             ft.IconButton(icon=ft.Icons.HOME, on_click=go_home),
#             back_button,
#             forward_button,
#             ft.IconButton(icon=ft.Icons.REFRESH, on_click=refresh),
#         ]
#     )
#     address_row = ft.Row(controls=[address])
#     auto_toolbar = ft.Row(controls=[auto_button, auto_status])
#     page.add(
#         ft.SafeArea(
#             expand=True,
#             content=ft.Column(
#                 expand=True,
#                 controls=[toolbar, address_row, auto_toolbar, browser],
#             ),
#         )
#     )


# if __name__ == "__main__":
#     ft.run(main)
