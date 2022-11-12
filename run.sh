if [ `basename $CONDA_PREFIX` != "env37" ]; then
    source `which activate` env37
    echo "Env: " `basename $CONDA_PREFIX`
fi

flask run