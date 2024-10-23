export const dropTables = `
  drop table if exists users;
  drop table if exists categories;
  drop table if exists posts;
  drop table if exists comments;
  drop table if exists likes;
`

export const createTables = `
  create table if not exists users (
    id integer primary key autoincrement,
    username text not null unique,
    email text not null unique,
    password_hash text not null,
    avatar_url text not null,
    created_at text default (datetime('now', 'utc'))
  );

  create table if not exists categories (
    id integer primary key autoincrement,
    name text not null unique
  );

  create table if not exists posts (
    id integer primary key autoincrement,
    user_id integer,
    category_id integer,
    caption text not null,
    image blob not null,
    created_at text default (datetime('now', 'utc')),
    foreign key (user_id) references users(id),
    foreign key (category_id) references categories(id)
  );

  create table if not exists comments (
    id integer primary key autoincrement,
    post_id integer,
    user_id integer,
    content text not null,
    created_at text default (datetime('now', 'utc')),
    foreign key (post_id) references posts(id),
    foreign key (user_id) references users(id)
  );

  create table if not exists likes (
    id integer primary key autoincrement,
    post_id integer,
    user_id integer,
    created_at text default (datetime('now', 'utc')),
    unique (post_id, user_id),
    foreign key (post_id) references posts(id),
    foreign key (user_id) references users(id)
  );
`

export const insertDummy = `
insert into
  users (username, email, password_hash, avatar_url)
values
  (
    'john_doe',
    'john@example.com',
    'hashed_password_1',
    'https://picsum.photos/31'
  ),
  (
    'jane_smith',
    'jane@example.com',
    'hashed_password_2',
    'https://picsum.photos/32'
  ),
  (
    'alice_wonder',
    'alice@example.com',
    'hashed_password_3',
    'https://picsum.photos/33'
  );
`
