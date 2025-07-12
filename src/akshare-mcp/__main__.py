import logging
from datetime import datetime, timezone

from fastmcp import FastMCP
from fastmcp.tools.tool import FunctionTool
import us
import hk
import cn


logger = logging.getLogger(__name__)


def main():
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
    mcp.add_tool(FunctionTool.from_function(cn.get_stock_zh_a_daily))
    # hk
    mcp.add_tool(FunctionTool.from_function(hk.get_stock_financial_hk_report_em))
    mcp.add_tool(FunctionTool.from_function(hk.get_stock_hk_hist))
    # us
    mcp.add_tool(FunctionTool.from_function(us.get_stock_financial_us_report_em))
    mcp.add_tool(FunctionTool.from_function(us.get_stock_us_daily))

    # mcp.run(transport="streamable-http", port=8902)
    mcp.run()


def get_datetime() -> str:
    """Get current date and time with timezone"""
    utc_now = datetime.now(timezone.utc)
    system_tz = utc_now.astimezone().tzinfo
    return datetime.now(tz=system_tz).strftime("%Y-%m-%d %H:%M:%S %z")

if __name__ == "__main__":
    main()