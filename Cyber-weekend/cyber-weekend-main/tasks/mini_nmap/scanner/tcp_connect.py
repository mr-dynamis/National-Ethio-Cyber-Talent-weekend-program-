import asyncio

async def tcp_scan(target, port, results):
    try:
        reader, writer = await asyncio.open_connection(target, port)
        results.append((port, "OPEN", "TCP"))
        writer.close()
        await writer.wait_closed()
    except:
        pass
