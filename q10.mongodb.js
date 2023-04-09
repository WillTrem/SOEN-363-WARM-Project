// Retrieve all tweets that contain a specific string (Instagram)

use("project-phase-3-db");

db.tweet.find({ text: { $regex: /Instagram/ } })
