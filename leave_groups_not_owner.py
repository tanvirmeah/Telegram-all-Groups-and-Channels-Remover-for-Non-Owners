from telethon.sync import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerChannel, Channel, ChatForbidden, InputPeerChat


# Get your own app ID and api_hash from https://my.telegram.org/apps | Create a bot using bot father and get your Bot token.
api_id = 000000
api_hash = 'app api_hash'
bot_token = 'your Bot token'

async def leave_groups():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        dialogs = await client(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerChannel(0, 0),
            limit=10,
            hash=0
        ))
        for dialog in dialogs.chats:
            try:
                if isinstance(dialog, Channel):
                    await client(LeaveChannelRequest(dialog.id))
                    print(f"Left group/channel: {dialog.title}")
                elif isinstance(dialog, ChatForbidden):
                    print(f"Cannot leave group/channel: {dialog.title}. You may lack permission or be banned.")
                else:
                    print(f"Cannot leave group/channel: {dialog.title}. It is not a channel.")
            except Exception as e:
                print(f"Failed to leave {dialog.title}: {str(e)}")

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(leave_groups())
