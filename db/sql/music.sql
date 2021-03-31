-- Table: public.music

-- DROP TABLE public.music;

CREATE TABLE public.music
(
    id integer NOT NULL,
    file_id text COLLATE pg_catalog."default" NOT NULL,
    right_answer text COLLATE pg_catalog."default" NOT NULL,
    wrong_answer text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT music_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.music
    OWNER to tsbgxbxm;


-- Constraint: music_pkey

-- ALTER TABLE public.music DROP CONSTRAINT music_pkey;

ALTER TABLE public.music
    ADD CONSTRAINT music_pkey PRIMARY KEY (id);

