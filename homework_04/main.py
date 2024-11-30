import asyncio
from models import engine, Base, SessionLocal, User, Post
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def add_data_to_db(users_data, posts_data):
    async with SessionLocal() as session:
        users = [User(name=user['name'], username=user['username'], email=user['email']) for user in users_data]
        session.add_all(users)
        await session.commit()

        posts = [Post(user_id=post['userId'], title=post['title'], body=post['body']) for post in posts_data]
        session.add_all(posts)
        await session.commit()

async def async_main():
    await create_tables()
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    await add_data_to_db(users_data, posts_data)

def main():
    asyncio.run(async_main())