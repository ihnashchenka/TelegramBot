-- Table: public.users

-- DROP TABLE public.users;

CREATE TABLE public.users
(
    id text COLLATE pg_catalog."default" NOT NULL,
    file_id text COLLATE pg_catalog."default" NOT NULL,
    right_answer text COLLATE pg_catalog."default" NOT NULL,
    wrong_answer text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT users_id_key UNIQUE (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.users
    OWNER to tsbgxbxm;
	
-- Constraint: users_id_key

-- ALTER TABLE public.users DROP CONSTRAINT users_id_key;

ALTER TABLE public.users
    ADD CONSTRAINT users_id_key UNIQUE (id);
