# poc-emmental

This is the emmental version of the poc building a tiny stack as our feedback-main project. Purpose is to let dev start from there to fill the holes and build the wished features.

## Features to develop

- A Flask API `http://localhost:80/reviews` that reads existing review database

- A welcome/search page allowing users to search the reviews by keywords on `http://localhost:3000/reviews?keywords=<keywords>`

  <img
    alt="reviews"
    src="https://raw.githubusercontent.com/feedback-news/poc-emmental/master/images/reviews.png"
    style="border: 1px solid black;float:left;"
    width="50%"
  />
  <img
    alt="reviews with keywords"
    src="https://raw.githubusercontent.com/feedback-news/poc-emmental/master/images/reviews_with_keywords.png"
    style="border: 1px solid black;float:right;"
    width="50%"
  />

- A Page template for each review `http://localhost:3000/reviews/<reviewId>` listing all the instances repeating the claim or content, all the social media accounts having spread it. If there is time, possibility of he user to add an other appearance.

  <img
    alt="review"
    src="https://raw.githubusercontent.com/feedback-news/poc-emmental/master/images/review.png"
    style="border: 1px solid black;float:left;"
    width="50%"
  />
  <img
    alt="review with appearance"
    src="https://raw.githubusercontent.com/feedback-news/poc-emmental/master/images/review_with_appearance.png"
    style="border: 1px solid black;float:right;"
    width="50%"
  />

<div/>

qsdqd

## Design inspiration

<img alt="design" src="https://raw.githubusercontent.com/feedback-news/poc-emmental/master/images/design.png" width="100%"/>

## Tech tasks

- run a docker-compose of two containers: one for the python flask api, and one for the postgres

- use ./poc start

- write api/app.py and TBW backend

- write webapp
