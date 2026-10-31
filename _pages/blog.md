---
layout: archive
title: ""
permalink: /blog/
author_profile: true
---

<style>
.blog-entry {
  margin-bottom: 2.5em;
  padding-bottom: 2em;
  border-bottom: 1px solid #e5e7eb;
}
.blog-venue {
  font-size: 0.8em;
  font-weight: bold;
  color: #1d4ed8;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.4em;
}
.blog-title {
  font-size: 1.1em;
  font-weight: bold;
  margin-bottom: 0.3em;
}
.blog-title a {
  color: #111;
  text-decoration: none;
}
.blog-title a:hover {
  text-decoration: underline;
}
.blog-author {
  font-size: 0.88em;
  color: #555;
  margin-bottom: 0.8em;
}
.blog-body {
  display: flex;
  gap: 1.2em;
  align-items: flex-start;
}
.blog-body img {
  width: 300px;
  min-width: 300px;
  border-radius: 4px;
  border: 1px solid #e5e7eb;
}
.blog-excerpt {
  font-size: 0.9em;
  color: #444;
  line-height: 1.6;
}
</style>

# Blog Posts

<div class="blog-entry">
  <div class="blog-venue">🛰️ Cisco ThousandEyes Engineering · October 20, 2026</div>
  <div class="blog-title"><a href="https://medium.com/thousandeyes-engineering/extending-end-point-event-detection-to-cellular-networks-what-we-learned-2916dd6e66de" target="_blank">Extending End Point Event Detection to Cellular Networks: What We Learned</a></div>
  <div class="blog-body">
    <img src="{{ site.baseurl }}/images/blog-thousandeyes-cellular.png" alt="Cellular event detection at Cisco ThousandEyes">
    <div class="blog-excerpt">During my internship on the Internet Measurement Research team, I extended ThousandEyes' Event Detection pipeline to Android agents measuring over 4G/5G. Cellular networks hide the radio access network inside GTP tunnels and mask the real gateway infrastructure behind session-specific IP addresses, so the system could tell that cellular was involved but not where inside the network a failure occurred. The post covers what we built, what we found, and the RAN visibility and gateway mapping needed for end-to-end cellular event detection.</div>
  </div>
</div>

<div class="blog-entry">
  <div class="blog-venue">🌍 Internet Society Pulse · August 11, 2026</div>
  <div class="blog-title"><a href="https://pulse.internetsociety.org/en/blog/2026/08/why-ip-geolocation-cant-be-trusted-for-mobile-networks-and-the-global-south/" target="_blank">Why IP Geolocation Can't Be Trusted for Mobile Networks and the Global South</a></div>
  <div class="blog-body">
    <img src="{{ site.baseurl }}/images/blog-geolocation-fig2.png" alt="Geolocation failure rates by region">
    <div class="blog-excerpt">Mobile network geolocation errors are more than 10× worse than fixed broadband, with Africa and Asia seeing failure rates of 66–72% and 53–61% respectively, compared to under 20% in Europe. The problem is structural and provider-independent: geolocation prefixes covering mobile networks span vast geographic areas, and coarser address blocks are two to three times more prevalent in the Global South than in the Global North.</div>
  </div>
</div>
