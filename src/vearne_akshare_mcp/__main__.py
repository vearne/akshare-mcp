import logging
from datetime import datetime, timezone
from fastmcp import FastMCP
from fastmcp.tools.tool import FunctionTool
import argparse

import us
import hk
import cn


logger = logging.getLogger(__name__)


def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description="An MCP server capable of retrieving A-share, Hong Kong stock, and U.S. stock data using AkShare.")
    parser.add_argument("--bind", default="127.0.0.1", help="Specify the IP address to bind to (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8902, help="Specify the port number (default: 8902)")
    parser.add_argument("--http", action="store_true", help="Enable http server")

    # 解析命令行参数
    args = parser.parse_args()

    mcp = create_mcp()
    if args.http:
        mcp.run(transport="streamable-http", port=8902)
    else:
        mcp.run()

def create_mcp() -> FastMCP:
    mcp = FastMCP(name="akshare-mcp")
    # base
    mcp.add_tool(FunctionTool.from_function(get_datetime))

    # cn
    mcp.add_tool(FunctionTool.from_function(cn.get_stock_profit_sheet_by_yearly_em))
    mcp.add_tool(FunctionTool.from_function(cn.get_stock_profit_sheet_by_quarterly_em))
    mcp.add_tool(FunctionTool.from_function(cn.get_stock_profit_sheet_by_report_em))
    mcp.add_tool(FunctionTool.from_function(cn.get_stock_cash_flow_sheet_by_yearly_em))
    mcp.add_tool(FunctionTool.from_function(cn.get_stock_cash_flow_sheet_by_quarterly_em))
    mcp.add_tool(FunctionTool.from_function(cn.get_stock_cash_flow_sheet_by_report_em))
    mcp.add_tool(FunctionTool.from_function(cn.get_stock_balance_sheet_by_yearly_em))
    mcp.add_tool(FunctionTool.from_function(cn.get_stock_balance_sheet_by_report_em))
    mcp.add_tool(FunctionTool.from_function(cn.get_stock_zh_a_hist))
    # hk
    mcp.add_tool(FunctionTool.from_function(hk.get_stock_financial_hk_report_em))
    mcp.add_tool(FunctionTool.from_function(hk.get_stock_hk_hist))
    # us
    mcp.add_tool(FunctionTool.from_function(us.get_stock_financial_us_report_em))
    mcp.add_tool(FunctionTool.from_function(us.get_stock_us_hist))
    return mcp

def get_datetime() -> dict:
    """Get current date and time with timezone"""
    utc_now = datetime.now(timezone.utc)
    system_tz = utc_now.astimezone().tzinfo
    return {
        "result": datetime.now(tz=system_tz).strftime("%Y-%m-%d %H:%M:%S %z")
    }

if __name__ == "__main__":
    main()