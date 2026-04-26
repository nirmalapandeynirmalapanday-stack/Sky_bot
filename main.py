import asyncio
from clients import source_app, target_app, source_calls, target_calls
from config import SOURCE_GROUP, OWNER_ID
from chat_state import authorized_users
from bridge import source_join
import commands

async def main():
    print("🚀 Starting...")
    authorized_users.add(OWNER_ID)
    
    await source_app.start()
    await target_app.start()
    await source_calls.start()
    await target_calls.start()
    
    try:
        await source_join()
        print("✅ Source Joined!")
    except Exception as e:
        print(f"Source: {e}")
    
    print("✅ Bot Ready!")
    await asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    asyncio.run(main())
