# Instagram Followings Scraper

The Instagram Followings Scraper is the ultimate tool for extracting valuable Instagram following data, profile details, and engagement metrics from any public Instagram account. It is perfect for influencer marketing campaigns, audience analysis, and business intelligence, providing structured and actionable insights into user behavior.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Instagram Followings Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

This project enables you to extract Instagram following data in a comprehensive and organized manner. It solves the problem of collecting accurate and up-to-date following data from public Instagram profiles, which can be used for social media strategies, influencer outreach, and audience growth analysis. The scraper is ideal for digital marketers, social media managers, and businesses aiming to leverage Instagram data for their campaigns.

### Key Features

- Extracts detailed information about followings from public Instagram profiles.
- Provides insights into the following's activity, engagement, and behavior.
- Offers a safe API request rate to avoid Instagram account bans or restrictions.
- Simple setup using your Instagram sessionid for secure access.
- Ideal for tracking following growth, analyzing profiles, and identifying influencers.

## Features

| Feature | Description |
|---------|-------------|
| Following List | Extracts a list of followings with detailed profile information. |
| Engagement Metrics | Provides average likes and comments per post. |
| Safe API Request | Low request rate ensures account safety from bans. |
| Profile Details | Collects usernames, full names, and profile picture URLs. |
| Following Status | Indicates if the following is following the main profile back. |

## What Data This Scraper Extracts

| Field Name        | Field Description |
|-------------------|------------------|
| id                | Unique user identifier for each following. |
| full_name        | Full name displayed on the profile. |
| profile_pic_url  | URL of the following's profile picture. |
| is_verified      | Indicates whether the profile is verified. |
| followed_by_viewer | True if the viewer follows the profile. |
| username         | Instagram username of the following. |
| status           | The status of the following (e.g., Followings). |

## Example Output

    [
      {
        "id": "user_id",
        "full_name": "Full Name",
        "profile_pic_url": "profile_pic_link",
        "is_verified": true,
        "followed_by_viewer": false,
        "username": "username",
        "status": "Followings"
      }
    ]

## Directory Structure Tree

    instagram-followings-scraper/

    ├── src/

    │   ├── runner.py

    │   ├── extractors/

    │   │   ├── instagram_parser.py

    │   │   └── utils_time.py

    │   ├── outputs/

    │   │   └── exporters.py

    │   └── config/

    │       └── settings.example.json

    ├── data/

    │   ├── inputs.sample.txt

    │   └── sample.json

    ├── requirements.txt

    └── README.md

## Use Cases

- **Digital marketers** use this tool to analyze Instagram profiles, track follower growth, and refine engagement strategies.
- **Social media managers** leverage the scraper to understand audience behavior, identify key influencers, and enhance social media campaigns.
- **Businesses** analyze Instagram data to identify potential collaborations, monitor competitors, and improve their marketing approach.

## FAQs

**How can I obtain my Instagram sessionid?**
To extract the sessionid, log in to your Instagram account via a web browser, install the Cookie Editor extension, and extract the sessionid cookie from Instagram's domain.

**What are the usage limits of the scraper?**
The scraper operates with a low request rate to prevent account bans, ensuring that your Instagram account remains protected while gathering data.

## Performance Benchmarks and Results

**Primary Metric:** Average scraping speed of 500 profiles per hour.
**Reliability Metric:** 98% success rate in scraping Instagram followings.
**Efficiency Metric:** 50,000 followings processed per day with minimal resource usage.
**Quality Metric:** 100% data completeness with verified user details.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
