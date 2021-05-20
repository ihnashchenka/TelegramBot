-- Table: public.users

-- DROP TABLE public.users;

CREATE TABLE public.users
(
    "U_ID" integer NOT NULL,
    "WIN_COUNT" integer NOT NULL DEFAULT 0,
    "GAME_COUNT" integer NOT NULL DEFAULT 0,
    CONSTRAINT "USER_ID" PRIMARY KEY ("U_ID")
)

TABLESPACE pg_default;
