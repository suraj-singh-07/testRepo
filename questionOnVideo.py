import os
import subprocess

try:
    # to make a video file with question
    subprocess.call(['ffmpeg','-f','lavfi','-i','color=black:1280x720, drawtext=textfile=question1.txt:x=(main_w-text_w)/2:y=(main_h-text_h)/2:fontcolor=FFFFFF:fontsize=25:,fade=t=in:st=0:d=1,fade=t=out:st=3:d=1','-t', '5','question1Video.mp4'])

    # to scale the question file
    subprocess.call(['ffmpeg','-i','question1Video.mp4','-vf','scale=1280:720','-preset','slow','-crf','18','question1VideoScaled.mp4'])
    subprocess.call(['rm','question1Video.mp4'])

    # adding question as subtitle in the main video
    subprocess.call(['ffmpeg', '-i', 'test_video.mp4', '-vf', "drawtext=textfile=question1.txt:x=(w-text_w)/2:y=(h-th-10):fontsize=50:fontcolor=white", '-c:a', 'copy', 'test_videoWithQuestion.mp4'])

    # to scale the main video
    subprocess.call(['ffmpeg','-i','test_videoWithQuestion.mp4','-vf','scale=1280:720','-preset','slow','-crf','18','test_videoScaled.mp4'])
    subprocess.call(['rm','test_videoWithQuestion.mp4'])

    # finally concatinating the both file
    subprocess.call(['ffmpeg','-f','concat','-safe','0','-i','concat.txt','-c','copy','FinalVideo.mp4'])
    subprocess.call(['rm','question1VideoScaled.mp4'])
    subprocess.call(['rm','test_videoScaled.mp4'])

except:
    print('Error in Creating first question Video')


try: 
    # to make a video file with question
    subprocess.call(['ffmpeg','-f','lavfi','-i','color=black:1280x720, drawtext=textfile=question2.txt:x=(main_w-text_w)/2:y=(main_h-text_h)/2:fontcolor=FFFFFF:fontsize=25:,fade=t=in:st=0:d=1,fade=t=out:st=3:d=1','-t', '5','question2Video.mp4'])

    # to scale the question file
    subprocess.call(['ffmpeg','-i','question2Video.mp4','-vf','scale=1280:720','-preset','slow','-crf','18','question2VideoScaled.mp4'])
    subprocess.call(['rm','question2Video.mp4'])

    # adding question as subtitle in the main video
    subprocess.call(['ffmpeg', '-i', 'test_video.mp4', '-vf', "drawtext=textfile=question2.txt:x=(w-text_w)/2:y=(h-th-10):fontsize=50:fontcolor=white", '-c:a', 'copy', 'test_videoWithQuestion2.mp4'])

    # to scale the main video
    subprocess.call(['ffmpeg','-i','test_videoWithQuestion2.mp4','-vf','scale=1280:720','-preset','slow','-crf','18','test_videoScaled2.mp4'])
    subprocess.call(['rm','test_videoWithQuestion2.mp4'])

    # finally concatinating the both file
    subprocess.call(['ffmpeg','-f','concat','-safe','0','-i','concat2.txt','-c','copy','FinalVideo2.mp4'])
    subprocess.call(['rm','question2VideoScaled.mp4'])
    subprocess.call(['rm','test_videoScaled2.mp4'])

except:
    print('Error in creating second question video')


subprocess.call(['ffmpeg','-f','concat','-safe','0','-i','concat3.txt','-c','copy','FinalVideo3.mp4'])
subprocess.call(['rm','FinalVideo.mp4'])
subprocess.call(['rm','FinalVideo2.mp4'])
