opencv_createsamples -info positive.info -bg negative.txt -vec new.vec -num 141 -w 640 -h 480
if [ $? -ne 0 ]; then
	exit $?
fi
