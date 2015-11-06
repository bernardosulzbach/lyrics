.mode column
.header on
select artist, round(avg(score_delta), 3) as mean_score_delta from playing_data group by artist;
