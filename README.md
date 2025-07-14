# akshare-mcp
an MCP server capable of retrieving A-share, Hong Kong stock, and U.S. stock data using AkShare.

## Usage
### 1. Install and Run
```
pip install vearne-akshare-mcp
```
### Method 1: Run with transport 'stdio'
```
python3 -m vearne_akshare_mcp
```
### Method 2: Run with transport 'streamable-http'
```
python3 -m vearne_akshare_mcp --http --bind="127.0.0.1" --port=8090
```
Server URL: http://127.0.0.1:8090/mcp/

### 2. use with uvx
``` 
"mcpServers": {
    "vearne-akshare-mcp": {
        "command": "uvx",
        "args": ["vearne_akshare_mcp"]
    }
}
```

## Thanks
[akfamily/akshare](https://github.com/akfamily/akshare)

## Inspired by akshare-one-mcp
[zwldarren/akshare-one-mcp](https://github.com/zwldarren/akshare-one-mcp)
