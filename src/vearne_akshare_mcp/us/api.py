import akshare as ak
from pydantic import Field
from typing import Annotated, Literal


def get_stock_financial_us_report_em(
        stock: Annotated[str, Field(description="Stock symbol (e.g. 'TSLA')")],
        symbol: Annotated[
            Literal["资产负债表", "综合损益表", "现金流量表"],
            Field(description="报表类型")
        ],
        indicator: Annotated[
            Literal["年报", "单季报", "累计季报"],
            Field(description="时间维度")
        ],
        recent_n: Annotated[
            int | None,
            Field(description="返回最近 N 条记录", ge=1)
        ] = 10,
) -> str:
    """
        美股
        东方财富-美股-财务分析-三大报表
        https://emweb.eastmoney.com/PC_USF10/pages/index.html?code=TSLA&type=web&color=w#/cwfx
    """
    df = ak.stock_financial_us_report_em(stock=stock,symbol=symbol,indicator=indicator)
    if recent_n is not None:
        df = df.head(recent_n)
    return df.to_json(orient="records")


def get_stock_us_hist(
        symbol: Annotated[str, Field(description="Stock symbol (e.g. '105.MSFT')")],
        start_date: Annotated[str, Field(description="start date (e.g. '20201103')")],
        end_date: Annotated[str, Field(description="end date (e.g. '20251103')")],
        adjust: Annotated[str, Literal["qfq", "hfq", "hfq-factor", "qfq-factor", ""],
            Field(description="默认为空: 返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据; hfq-factor: 返回后复权因子; qfq-factor: 返回前复权因子")],
) -> str:
    """
        美股
        东方财富网-行情-美股-每日行情
        https://quote.eastmoney.com/us/ENTX.html#fullScreenChart
    """
    df = ak.stock_us_hist(symbol=symbol, start_date=start_date, end_date=end_date, adjust=adjust)
    return df.to_json(orient="records")
