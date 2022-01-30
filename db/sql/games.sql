-- Table: public.games

-- DROP TABLE public.games;

CREATE TABLE public.games
(
    "G_ID" integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    "USER_ID" integer NOT NULL,
    "MUSIC_ID" integer NOT NULL,
    "ANSWERS" character varying(400)[] COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT game_id PRIMARY KEY ("G_ID"),
    CONSTRAINT music_fkey FOREIGN KEY ("MUSIC_ID")
        REFERENCES public.music ("M_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT user_fkey FOREIGN KEY ("USER_ID")
        REFERENCES public.users ("U_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;