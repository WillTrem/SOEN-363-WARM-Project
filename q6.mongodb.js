// Count the total number of tweets posted by a specific user.

use("project-phase-3-db");

db.tweets.countDocuments({ userId: 5 });