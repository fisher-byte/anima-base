---
guest: Brian Chesky
title: Brian Chesky's new playbook
youtube_url: https://www.youtube.com/watch?v=4ef0juAMqoE
video_id: 4ef0juAMqoE
publish_date: 2023-11-12
description: 'Brian Chesky is the co-founder and CEO of Airbnb. Under Brian's leadership, Airbnb has grown into a community of over 4 million hosts who have welcomed more than 1.5 billion guests across...'
duration_seconds: 4408.0
duration: '1:13:28'
view_count: 381905
channel: Lenny's Podcast
date_collected: 2026-03-11
collection_source: ChatPRD/lennys-podcast-transcripts
language: en
status: full_transcript
---

# Brian Chesky's new playbook

## Transcript

Brian Chesky (00:00:00):
Way too many founders apologize for how they want to run the company. They find some midpoint between how they want to run a company and how the people they lead want to run the company. That's a good way to make everyone miserable. Because what everyone really wants is clarity. And what everyone really wants is to be able to row in the same direction really quickly. And so I basically got involved in every single detail and I basically told leaders that leaders are in the details. And there's this negative term called micromanagement. I think there's a difference between micromanagement, which is like telling people exactly what to do, and being in the details. Being in the details is what every responsible company's board does to the CEO. That doesn't mean the board is telling them what to do. But if you don't know the details, how do you know people are doing a good job? People think that great leader's job is to hire people and just empower them to do a good job. Well, how do you know they're doing a good job if you're not in the details? And so I made sure I was in the details and we really drove the product.

Lenny (00:01:01):
Today my guest is Brian Chesky. Brian is the CEO and co-founder of Airbnb, which he started in his apartment with his co-founders, Joe and Nate, and has turned into an $80 billion global business with travelers and homes in 220 countries. I was very lucky to get to work with Brian for many years, and my sense is if you ask people who they consider the most inspiring tech or business leaders today, Brian would be right near the top of that list.

(00:01:27):
In our conversation, Brian shares an in-depth explanation of what's happening with product management at Airbnb, which caused quite a stir in the product world when he talked about this previously. We also get deep into Brian's new approach of how he runs Airbnb, including shifting away from traditional growth channels like paid growth, and instead betting that if they just build the best possible product and tell people about it, growth will happen. Also, how the product team now operates including having just one single roadmap across the entire company and Brian staying very close to every design and every feature. We also get a bit into his personal life, including how he finds balance and avoids burnout, how he continues to learn himself so that he can stay ahead of business and its growth. This is a very special episode for me and I'm thrilled to bring you Brian Chesky after a short word from our sponsors.

(00:02:17):
This episode is brought to you by Sidebar. Are you looking to land your next big career move or start your own thing? One of the most effective ways to create a big leap in your career and something that worked really well for me a few years ago is to create a personal board of directors. A trusted peer group where you can discuss challenges you're having, get career advice, and just gut check how you're thinking about your work, your career, and your life. This has been a big trajectory changer for me, but it's hard to build this trusted group. With Sidebar, senior leaders are matched with highly vetted, private, supportive peer groups to lean on for unbiased opinions, diverse perspectives, and raw feedback. Everyone has their own zone of genius, so together we're better prepared to navigate professional pitfalls leading to more responsibility, faster promotions, and bigger impact.

(00:03:06):
Guided by world-class programming and facilitation, Sidebar enables you to get focused, tactical feedback at every step of your journey. If you're a listener of this podcast, you're likely already driven and committed to growth. A Sidebar personal board of directors is the missing piece to catalyze that journey. Why spend a decade finding your people when you can meet them at Sidebar today. Jump the growing wait list of thousands of leaders from top tech companies by visiting sidebar.com/lenny to learn more. That's sidebar.com/lenny.

(00:03:38):
You fell in love with building products for a reason, but sometimes the day-to-day reality is a little different than you imagined. Instead of dreaming up big ideas, talking to customers and crafting a strategy, you're drowning in spreadsheets and roadmap updates and you're spending your days basically putting out fires. A better way is possible. Introducing Jira Product Discovery, the new prioritization and roadmapping tool built for product teams by Atlassian.

(00:04:04):
With Jira Product Discovery, you can gather all your product ideas and insights in one place and prioritize confidently finally, replacing those endless spreadsheets. Create and share custom product roadmaps with any stakeholder in seconds and it's all built on Jira where your engineering team's already working so true collaboration is finally possible. Great products are built by great teams, not just engineers. Sales, support, leadership, even Greg from finance. Anyone that you want can contribute ideas, feedback, and insights in Jira Product Discovery for free. No catch. And it's only $10 a month for you. Say goodbye to your spreadsheets and the never ending alignment efforts. The old way of doing product management is over. Rediscover what's possible with Jira Product Discovery. Try for free at atlassian.com/lenny. That's atlassian.com/lenny.

(00:05:00):
Brian, thank you so much for being here. Welcome to the podcast.

Brian Chesky (00:05:04):
Well, thank you for having me.

Lenny (00:05:06):
Did you ever think when I left Airbnb, one, that I would have a podcast and two, that you would be on my podcast?

Brian Chesky (00:05:12):
I had no idea you would become a podcast host and that you would have such a successful podcast. But yeah, congrats on everything. This is awesome.

Lenny (00:05:18):
I appreciate it. Congrats to you too, Brian. Things seem to be going great. I'm excited that you're here. I want to start with the elephant in the room for a lot of listeners of this podcast. What is going on with product management at Airbnb? You made some comments at Figma Config and a lot of people got this impression that you eliminated product management at Airbnb, and I've heard from a lot of product execs having boardroom conversations as a result of that. And they were trying to decide should we remove product management from the company? Should we significantly cut product management? So I'm just curious to hear from you, what is the latest on your thinking on product management and what's happening with product management at Airbnb?

Brian Chesky (00:05:56):
I spoke at Figma four or five months ago. I spoke to a room of designers. I then got off-stage. I saw somebody tweet that said something to the nature of that I said I got rid of the product management function and all the designers in the room started cheering. So I want to talk about two things. What I actually meant, because I didn't actually get rid of the people. And also why did the people in the room cheer? Because that's also a thing we should ask ourselves. And I hope everyone listening to this podcast should understand where did that place come from, that 5,000 designers in a room cheered because they thought I eliminated the existence of a function? Because if I said I eliminated the engineering function, no one would've cheered. It was specifically that function. So I want to talk about what that might mean. It wasn't the people, it's the way they're working together.

(00:06:46):
So we don't have any longer the traditional product management function as it existed when you was here. But we didn't get rid of people helping drive the product. What we did is we combined what one might call the inbound product development responsibilities of product manager with the outbound or marketing responsibilities of product marketing. That's the first thing we did. The second thing we did is we off boarded much of the program management functions that product managers may do to actual program managers. A lot of people with the product management title are actually program managers. So we actually started off boarding some responsibilities to program management. The last thing we did is we made the group smaller and more senior. So we don't really have a lot of junior product marketers. So the most senior people are called product marketers, but everyone has to understand how to talk about the product.

(00:07:42):
So the basic idea is this. You can't build a product unless you know how to talk about the product. And you can't talk about the product unless you know how to build it. So we basically said, let's combine those functions. And the reason why is because one of the biggest problems we had at Airbnb was we would build things and then we would hand it to marketing and then marketing would come back and say, well, I can't market this because you didn't build it the right way. Or marketing would come up with an idea and throw it over the fence to product and say, build this. And so by combining the functions, we eliminated the handoffs.

## Source Information

- **Original Video**: [YouTube](https://www.youtube.com/watch?v=4ef0juAMqoE)
- **Channel**: Lenny's Podcast
- **Published**: 2023-11-12
- **Duration**: 1:13:28
- **Views**: 381,905
- **Transcript Source**: ChatPRD/lennys-podcast-transcripts
- **Collected**: 2026-03-11

---
*Full transcript available at source repository*
