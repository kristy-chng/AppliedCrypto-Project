# AppliedCrypto-Project

NTU School of Computer Science and Engineering (AY2021/22 S1)  
CZ4010 Applied Cryptography

This project is developed in accordance to the course project of CZ4010 Applied Cryptography.   
**Title**: Implementation &amp; Analysis of Henon Map on Image Encryption

### Motivation
Many different algorithms such as AES and DES have been seen to be used for data encryption. However, as digital images have different characteristics as compared to conventional text data, more specialised algorithms are needed in order to encrypt them. 


### Research
As such, research works have led to the study of the linkage of traditional cryptography and chaos theory. Chaotic values are seen to be useful in encryption processes as it is generally easy to generate long chaotic pseudorandom sequences whose values seems to be uncorrelated (if the initial values and related parameters used for sequence generation are not known) - making it comparatively faster than other algorithms. 

One such example of a chaotic system is the Henon Map. This is a symmetric and deterministic system that creates pseudorandom sequences required for encryption via a chaotic equation. The equation is as follows:

- Where the system is only unpredictable if a = 1.4 & b = 0.3
- Initial points X1 & Y1 serves as the symmetric keys


### Design & Development
A web application has been developed for users to have the ability to encrypt and decrypt images files (.png) using the Henon Map Chaotic System. Development is done using HTML+CSS as the front-end, Python as the back-end and the Flask Framework to integrate both front-end and back-end together. Atom (on Mac) was used as the code editor of choice.

For the front-end, there are 3 main folders of interest:  
1. styles: contains the style sheets for each web page  
2. uploads: stores images for display purposes; saved encrypted and decrypted images are stored here too  
3. templates: contains the structure for each web page (about page, encrypt page, decrypt page)  

For the back-end, there are 3 main files of interest:  
1. main.py: the main code to run the sever  
2. chaosTheory.py: provides the algorithm for image encryption/decryption and is used by main.py  
3. analysis.ipynb: a Jupyter notebook that provides the code for the analysis portion of the project  

*Currently works on .png files and images with equal length-width dimensions; some sample images can be found on the sampleImages folder


### Instructions
1. Download the source code onto your local computer
2. Ensure that the following libraries have been installed: Flask, Pillow, cv2, numpy
3. Navigate to the file directory of the source code
4. Run main.py
5. Open your browser of choice and head to http://127.0.0.1:5000/



