CREATE TABLE IF NOT EXISTS "products" (
  id          VARCHAR(255) PRIMARY KEY NOT NULL,
  user_id     VARCHAR(255) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  name        VARCHAR(50)  NOT NULL,
  description VARCHAR(255) NOT NULL,
  price       INTEGER      NOT NULL,
  status      VARCHAR(10)  NOT NULL DEFAULT 'active',
  category_id VARCHAR(255) NOT NULL REFERENCES categories(id) ON DELETE CASCADE,
  created_at  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE "products" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");
ALTER TABLE "products" ADD FOREIGN KEY ("category_id") REFERENCES "categories" ("id");