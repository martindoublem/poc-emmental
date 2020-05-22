# poc-emmental 

This is the emmental version of the poc building a tiny stack as our feedback-main project. Purpose is to let dev start from there to fill the holes and build the wished features.

## Features to develop

- A Flask API `http://localhost:80/reviews` that reads existing review database

- A welcome/search page allowing users to search the reviews by keywords on `http://localhost:3000/reviews?keywords=<keywords>`:
<p align="center">
  <kbd>
    <img
      alt="reviews"
      src="https://raw.githubusercontent.com/feedback-news/poc-emmental/master/images/reviews.png"
    />
  </kbd>
</p>

- A welcome/search page allowing users to search the reviews by keywords on `http://localhost:3000/reviews?keywords=<keywords>`:  
<p align="center">
  <kbd>
    <img
      alt="reviews with keywords"
      src="https://raw.githubusercontent.com/feedback-news/poc-emmental/master/images/reviews_with_keywords.png"
    />
  </kbd>
</p>

- A Page template for each review `http://localhost:3000/reviews/<reviewId>` listing all the instances repeating the claim or content, all the social media accounts having spread it:
<p align="center">
  <kbd>
    <img
      alt="review"
      src="https://raw.githubusercontent.com/feedback-news/poc-emmental/master/images/review.png"
    />
  </kbd>
</p>

- If there is time, possibility of he user to add an other appearance:
<p align="center">
  <kbd>
    <img
      alt="review with appearance"
      src="https://raw.githubusercontent.com/feedback-news/poc-emmental/master/images/review_with_appearance.png"
    />
  </kbd>
</p>

## Design inspiration

Respect the design of:

<p align="center">
  <kbd>
    <img
      alt="design"
      src="https://raw.githubusercontent.com/feedback-news/poc-emmental/master/images/design.png"
    />
  </kbd>
</p>

## Model

- Content Claim and appearance on:
<p align="center">
  <kbd>
    <img
      alt="reviews"
      src="https://raw.githubusercontent.com/feedback-news/poc-emmental/master/images/ontology_1.png"
    />
  </kbd>
</p>

- Review:
<p align="center">
  <kbd>
    <img
      alt="reviews"
      src="https://raw.githubusercontent.com/feedback-news/poc-emmental/master/images/ontology_2.png"
    />
  </kbd>
</p>

- Medium and Organization:
<p align="center">
  <kbd>
    <img
      alt="reviews"
      src="https://raw.githubusercontent.com/feedback-news/poc-emmental/master/images/ontology_3.png"
    />
  </kbd>
</p>


## Tech tasks

Please fill the TBW placeholders while:

  - run a docker-compose of two containers: one for the python flask api, and one for the postgres
    use ./poc start

  - write models and call ./poc sandbox

  - write api reviews route feature

  - write webapp features
