"""
Telegram all Groups and Channels Remover for Non-Owners

This Python script allows you to leave all Telegram groups and channels where you are not the owner using the Telethon library.

Copyright (c) 2024 Tanvir Meah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
