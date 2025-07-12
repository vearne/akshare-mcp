import akshare as ak
from pydantic import Field
from typing import Annotated

def get_stock_profit_sheet_by_yearly_em(
        symbol: Annotated[str, Field(description="Stock symbol (e.g. 'SH600519','SZ000025')")],
        recent_n: Annotated[
            int | None, Field(description="Number of most recent records to return", ge=1)
        ] = 10,
) -> str:
    """
        A股
        东方财富-股票-财务分析-利润表-按年度
        https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0
    """
    df = ak.stock_profit_sheet_by_yearly_em(symbol=symbol)
    if recent_n is not None:
        df = df.head(recent_n)
    return df.to_json(orient="records")


def get_stock_profit_sheet_by_quarterly_em(
        symbol: Annotated[str, Field(description="Stock symbol (e.g. 'SH600519','SZ000025')")],
        recent_n: Annotated[
            int | None, Field(description="Number of most recent records to return", ge=1)
        ] = 10,
) -> str:
    """
        A股
        东方财富-股票-财务分析-利润表-按单季度
        https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0
    """
    df = ak.stock_profit_sheet_by_quarterly_em(symbol=symbol)
    if recent_n is not None:
        df = df.head(recent_n)
    return df.to_json(orient="records")

def get_stock_profit_sheet_by_report_em(
        symbol: Annotated[str, Field(description="Stock symbol (e.g. 'SH600519','SZ000025')")],
        recent_n: Annotated[
            int | None, Field(description="Number of most recent records to return", ge=1)
        ] = 10,
) -> str:
    """
        A股
        东方财富-股票-财务分析-利润表-报告期
        https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0
    """
    df = ak.stock_profit_sheet_by_report_em(symbol=symbol)
    if recent_n is not None:
        df = df.head(recent_n)
    return df.to_json(orient="records")


def get_stock_cash_flow_sheet_by_yearly_em(
        symbol: Annotated[str, Field(description="Stock symbol (e.g. 'SH600519','SZ000025')")],
        recent_n: Annotated[
            int | None, Field(description="Number of most recent records to return", ge=1)
        ] = 10,
) -> str:
    """
        A股
        东方财富-股票-财务分析-现金流量表-按年度
        https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0
    """
    df = ak.stock_cash_flow_sheet_by_yearly_em(symbol=symbol)
    if recent_n is not None:
        df = df.head(recent_n)
    return df.to_json(orient="records")


def get_stock_cash_flow_sheet_by_quarterly_em(
        symbol: Annotated[str, Field(description="Stock symbol (e.g. 'SH600519','SZ000025')")],
        recent_n: Annotated[
            int | None, Field(description="Number of most recent records to return", ge=1)
        ] = 10,
) -> str:
    """
        A股
        东方财富-股票-财务分析-现金流量表-按单季度
        https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0
    """
    df = ak.stock_cash_flow_sheet_by_quarterly_em(symbol=symbol)
    if recent_n is not None:
        df = df.head(recent_n)
    return df.to_json(orient="records")

def get_stock_cash_flow_sheet_by_report_em(
        symbol: Annotated[str, Field(description="Stock symbol (e.g. 'SH600519','SZ000025')")],
        recent_n: Annotated[
            int | None, Field(description="Number of most recent records to return", ge=1)
        ] = 10,
) -> str:
    """
        A股
        东方财富-股票-财务分析-现金流量表-按报告期
        https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0
    """
    df = ak.stock_cash_flow_sheet_by_report_em(symbol=symbol)
    if recent_n is not None:
        df = df.head(recent_n)
    return df.to_json(orient="records")

def get_stock_balance_sheet_by_yearly_em(
        symbol: Annotated[str, Field(description="Stock symbol (e.g. 'SH600519','SZ000025')")],
        recent_n: Annotated[
            int | None, Field(description="Number of most recent records to return", ge=1)
        ] = 10,
) -> str:
    """
        A股
        东方财富-股票-财务分析-资产负债表-按年度
        https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0
    """
    df = ak.stock_balance_sheet_by_yearly_em(symbol=symbol)
    if recent_n is not None:
        df = df.head(recent_n)
    return df.to_json(orient="records")


def get_stock_balance_sheet_by_report_em(
        symbol: Annotated[str, Field(description="Stock symbol (e.g. 'SH600519','SZ000025')")],
        recent_n: Annotated[
            int | None, Field(description="Number of most recent records to return", ge=1)
        ] = 10,
) -> str:
    """
        A股
        东方财富-股票-财务分析-资产负债表-按报告期
        https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0
    """
    df = ak.stock_balance_sheet_by_report_em(symbol=symbol)
    if recent_n is not None:
        df = df.head(recent_n)
    return df.to_json(orient="records")

def get_stock_zh_a_daily(
        symbol: Annotated[str, Field(description="Stock symbol (e.g. 'SH600519','SZ000025')")],
        start_date: Annotated[str, Field(description="start date (e.g. '20201103')")],
        end_date: Annotated[str, Field(description="end date (e.g. '20251103')")],
        adjust: Annotated[str, Field(description="默认为空: 返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据; hfq-factor: 返回后复权因子; qfq-factor: 返回前复权因子")],
) -> str:
    """
        A股
        新浪财经-A 股-个股的历史行情数据
        https://finance.sina.com.cn/realstock/company/sh603843/nc.shtml
    """
    df = ak.stock_zh_a_daily(symbol=symbol, start_date=start_date, end_date=end_date)
    return df.to_json(orient="records")

