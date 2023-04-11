// Counts the total number of tweets posted by a specific user (userId: 5) from Twitter

use("project-phase-3-db");

db.tweets.countDocuments({ userId: 5 });