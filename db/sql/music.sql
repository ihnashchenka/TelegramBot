-- Table: public.music

-- DROP TABLE public.music;

CREATE TABLE public.music
(
    "ID" integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 0 MINVALUE 0 MAXVALUE 2147483647 CACHE 1 ),
    "FILE_ID" text COLLATE pg_catalog."default" NOT NULL,
    "NAME" text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT music_pkey PRIMARY KEY ("ID")
)

TABLESPACE pg_default;