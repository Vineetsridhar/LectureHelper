# LectureHelper
This project listens to your lecture and provides real time captions as well as suggested images and links. Built as a part of HackNJIT 2021
## Inspiration
Covid-19 brought an air of unfamiliarity to classrooms all over the world and movement to an online form of lecture created an awkward and socially tense learning environment. For students to have their inquiries addressed, they had to resort to using a zoom chat box which the professor would hardly check or they would risk rudely cutting off the professor to ask a question. This creates an unfair learning environment for students who struggle with social and general anxiety. So to confront this issue, our group created Lecture Monke. 
## What it does
To assist those struggling with anxiety, Lecture Monke takes away the tension of asking a question by highlighting important words in the spoken lecture and providing access to background information on the topic of study. All of the words said by the lecturer are transcribed onto an interactive GUI which highlights important words and provides links to important pieces of information. This allows students to interact with lecture information like never before. It will also help students appear more engaged in class because if they zone out and find that they've missed key important details, they can just scroll back in the transcription instead of ruining the flow of a lecture or needing to spend extra time after class watching a lecture recording. 
## How we built it
We built it using Flask and Python. We used GCP for their Speech to text API and Azure for their text analysis API. We used Socket.IO for bidirectional communication between the server and client. 

## Challenges we ran into
We faced many challenges when building this application. After spending hours trying to fix all dependency issues, we finally had both the live transcription working, and a flask server running. The problem was that they were running separately. We had to figure out how exactly we could port these live transcripts into the flask server. At first, we weren't even sure if we should use flask over something like tkinter, but we had HTML experience so we decided it would be the way to go. We figured out that we can use sockets to get the data from the api into the webpage, and finally found a way for the client and server to communicate. Another problem we were struggling with was bootstrap and jQuery. We were both new to these platforms, so it was hard to diagnose and fix issues. One such issue was getting the modal popup working. We faced a lot of jQuery issues when trying to do this, but figured it was just a flask issue. 

## Accomplishments that we're proud of
George is a Material Engineer at Rutgers, and has very little coding experience. It was a great experience for him to build a complicated application like this. Lecture Monke came out pretty well. It did everything we wanted it to do and we were happy we finished in time. 

## What we learned
During this project, we learned how to use so many technologies we had never used before. Mainly things like jQuery and SocketIO. In addition, we got more familiar with Google and Microsoft's APIs. 

## What's next for Lecture Monke
The next thing for Lecture Monke would be to continue to find ways to expedite learning in online and in person lectures by imagining new ways of interacting with lecture materials. Lecture Monke has the potential to assist many people affected by the anxieties associated with learning, and the future of Lecture Monke would seek to continue to create a more equitable learning environment.
