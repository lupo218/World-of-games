import Utils


def Points_of_winning(dif):
    try:
        with open(Utils.SCORES_FILE_NAME, "r") as f:  # red
            points = int(f.read()) # get val
            new_points = str(int(points) + ((dif * 3) + 5))

            with open(Utils.SCORES_FILE_NAME, "w") as w: # write new points
                w.write(new_points)
    except:                                     # create new file
        new_points =str(((dif * 3) + 5))
        with open(Utils.SCORES_FILE_NAME, "w") as f:  # write new points to a new file
            f.write(new_points)