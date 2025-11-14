# LinkedIn Profile Posts Bulk Scraper (No Cookies)⚡$2 per 1k

> A high-performance LinkedIn posts scraper that extracts complete post content, engagement metrics, media, reactions, and comments — all without requiring cookies or login credentials.
> This tool delivers fast, scalable LinkedIn data collection for research, analytics, and outreach workflows.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
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
  If you are looking for <strong>LinkedIn Profile Posts Bulk Scraper (No Cookies)⚡$2 per 1k</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

This project extracts posts and engagement data from LinkedIn profiles or company pages at scale.
It solves the challenge of collecting reliable LinkedIn post insights without authentication, manual exporting, or complex workarounds.
Ideal for marketers, researchers, analysts, sales teams, and automation builders who need accurate, real-time LinkedIn post data.

### High-Speed, No-Login LinkedIn Data Collection

- Scrapes posts from any profile or company URL without cookies or account access.
- Delivers fresh, uncached data in seconds.
- Supports optional scraping of reactions and comments.
- Provides media details, engagement metrics, authors, repost info, and more.
- Processes up to 6 profiles simultaneously for improved throughput.

## Features

| Feature | Description |
|---------|-------------|
| No-cookie scraping | Extract posts without needing to log in or provide cookies. |
| Full post data | Captures text, media, links, repost content, and attached documents. |
| Engagement insights | Retrieves likes, reactions breakdown, comments, and shares. |
| Optional comments scraping | Enable full comment extraction with depth control. |
| Optional reactions scraping | Collect detailed reaction metadata for each user. |
| Concurrency engine | Scrapes up to 6 profiles at the same time for speed. |
| Pricing efficiency | Only $2 per 1k posts, including add-ons. |
| Fresh results | Always pulls live, uncached data. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|------------|-------------------|
| id | Unique identifier of the LinkedIn post. |
| linkedinUrl | Direct URL to the original post. |
| content | Full text content of the post. |
| author | Profile metadata of the post author. |
| postedAt | Timestamp and derived post-age info. |
| postImages | List of images attached to the post. |
| document | Document metadata including title, cover images, and pages. |
| socialContent | Visibility and interaction settings for the post. |
| engagement | Likes, comments, shares, and reaction type counts. |
| reactions | Individual reaction entries with actor metadata. |
| comments | Comment objects containing text, timestamp, actor, and metrics. |

---

## Example Output


    {
      "type": "post",
      "id": "7329207003942125568",
      "linkedinUrl": "https://www.linkedin.com/posts/williamhgates_how-better-data-helped-us-cut-child-mortality",
      "content": "The leading causes of childhood death reveal a stark truth...",
      "author": {
        "publicIdentifier": "williamhgates",
        "name": "Bill Gates",
        "info": "Chair, Gates Foundation and Founder, Breakthrough Energy"
      },
      "postedAt": {
        "timestamp": 1747419119821,
        "date": "2025-05-16T18:11:59.821Z"
      },
      "engagement": {
        "likes": 2916,
        "comments": 328,
        "shares": 153
      },
      "reactions": [
        {
          "reactionType": "LIKE",
          "actor": { "name": "Rami Sfaxi" }
        }
      ],
      "comments": [
        {
          "id": "7331415234328371202",
          "commentary": "I respect what you do and I am wondering...",
          "actor": { "name": "Justin Martin" }
        }
      ]
    }

---

## Directory Structure Tree


    LinkedIn Profile Posts Bulk Scraper (No Cookies)⚡$2 per 1k/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── linkedin_posts_parser.py
    │   │   └── utils_datetime.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── inputs.sample.txt
    │   └── sample.json
    ├── requirements.txt
    └── README.md

---

## Use Cases

- **Marketing teams** analyze competitor content performance to refine editorial strategy and improve engagement.
- **Sales teams** identify high-signal posts to trigger outreach based on prospect activity or thought leadership topics.
- **Recruiters** monitor candidate or company activity to personalize communication and improve response rates.
- **Researchers** collect public discourse, sentiment indicators, and engagement trends across industries.
- **Founders and analysts** benchmark brand visibility and post traction over time for strategic decision-making.

---

## FAQs

**Does this scraper require password, cookies, or login?**
No. It operates without any authentication and still retrieves full post data, reactions, and comments.

**Can it extract all comments and reactions?**
Yes. Set `maxComments` or `maxReactions` to `0` to scrape all available items, or specify limits for faster output.

**Does it support company pages as well as personal profiles?**
Absolutely — both personal profiles and company pages are supported using their standard LinkedIn URLs.

**Are reposts or quote posts included?**
Yes. You can include or exclude quote posts and reposts using `includeQuotePosts` and `includeReposts`.

---

## Performance Benchmarks and Results

**Primary Speed Metric:**
Processes posts with an average turnaround of a few seconds per profile thanks to 6-thread concurrency.

**Reliability Metric:**
Maintains a high success rate with consistent extraction across profiles, including media-heavy posts.

**Efficiency Metric:**
Optimized threading ensures minimal delays even when scraping comments and reactions simultaneously.

**Quality Metric:**
Delivers complete post structures with rich metadata, offering strong accuracy in engagement counts, author data, and media extraction.


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
