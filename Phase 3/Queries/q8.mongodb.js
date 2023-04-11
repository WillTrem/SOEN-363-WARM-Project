// Lists users who have Instagram and Twitter with more than 2500 followers via Twitter

use("project-phase-3-db");

db.userTwitter.aggregate([
    {
        $lookup: 
        {
            from: "instagramaccount",
            localField: "username",
            foreignField: "username",
            as: "instagramaccount",
        },
    },
    {
        $match: 
        {
        
            followercount: { $gt: 2500 },
            instagramaccount: { $ne: [] },
        },
    },
    {
        $project:
           {
             _id: 0,
             username: "$username",
             number_Followers: "$followercount"
           }
     }
]).toArray();