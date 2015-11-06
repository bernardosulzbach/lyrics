.mode column
.header on
select artist, round(sum(cast(score_delta as real)) / sum(1.0), 3) as mean_score_delta from playing_data group by artist;
