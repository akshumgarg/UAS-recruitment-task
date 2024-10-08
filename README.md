# UAS-recruitment-task
# DAY 1 (02/10/2024)
As the task was needed to be done on github, I learnt the basic concepts about GitHub from youtube video:  
https://www.youtube.com/watch?v=RGOj5yH7evk  and https://www.youtube.com/watch?v=Ez8F0nW6S-w  

I learnt the basic concepts of making changes in repository through a code editor and other basic commands which will be used for the task.  
I made my own github repository and started coding in it through visual studio code.

# DAY 2 (03/10/2024)
I had already downloaded Python in my system. I also learnt about dictionary, list, strings etc in school. So, I skipped those parts and moved ahead.  
I started learning the required functions of numpy library from 
https://www.youtube.com/watch?v=Rbh1rieb3zc  

I learnt only the basic functions which I thought would be required in the task. I practiced some small and easy questions to get connected with this library.

# DAY 3 (04/10/2024) and DAY 4 (05/10/2024)
I spent my time to complete the pending assignments and practicals, so couldn't do much for the given task.

# DAY 5 (06/10/2024)
I learnt the basic functions of openCV and learnt how to separate a color from image(using HSV colorspace) from the following videos:  
https://www.youtube.com/watch?v=WQeoO7MI0Bs  
https://www.youtube.com/watch?v=Z78zbnLlPUA&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&t=1s  

and some documents as shown below:  
https://opencv.org/

# DAY 6 (07/10/2024)
Now, I started making the program.  

First, I needed to calculate the houses in burnt area and green area separately. So, I thought that I should make the masks of both the areas. By this, I could get the triangles in brown and green area (white and black in mask). Then I calculated the number of triangles in both the masks as done in code.  
My first plan was that I would calculate the number of contours which have 3 sides. But in the contours, triangles were not completely formed. In each triangle, two line were connected to each other and third one was separate.  
After many trials, I used another method. I calculated the area of contours and found the area of triangles from there. Since area of each triangle was same, I calculated the number of triangles which had that range of area.  
I made a function which could calculate the number of triangles in any mask/image. This was used a lot later.  
I have explained my code in the program itself, so that there will be no issue to the reader to read my code.  
Now, I had to find the number of red and blue houses in both burnt and green area to find priority. To do so, I made a separate mask of red triangles and added it to the mask of burnt area. This gave me the sum of blue burnt houses and red green houses. And by solving equations on paper, I got all the required values.  
Today, I made the code which could tell the number of burnt houses, green houses, priority of only one image at a time.  
I don't know why but one house in burnt area was not being counted in the contours. I couldn't solve this on time.

# DAY 7 (08/10/2024)
Now, I had to make this program applicable to all the images at the same time and to change green and brown color to different unique colors.  
I made the main part a function and kept cv2.imread part out of the function. This function returned all the required values which were later stored in different variables (can be seen in code). Then I made all the required lists and sorted them according to function. At last, to make order of images in last list, image2 and image11 had same priority, so only one image is shown in the list. I couldn't solve this issue on time.  

To change the brown and green colors to other colors, I used simple code (can be seen in code line 72,73)
