import numpy as np
import liveTools as lt
import matplotlib.pyplot as plt
# import kalmanTracking as lt

# a simple toy example for kalman tracking code which illustrates its use
#generates detections, sometimes adds new detections, sometimes misses detections
if __name__ == "__main__":
    detections = np.random.rand(1,2)*20
    tracker = lt.KF_Tracker(0.01) # 0.01 is delta_t
    tracked_objects = tracker(detections)
    # print(tracked_objects[0])
    colors = np.random.rand(1000,3)

    for i in range(0,500):
        # plot the points to visually confirm that it seems to be working

        x_coords = []
        y_coords = []
        for key in tracked_objects:
            x_coords.append(tracked_objects[key][0])
            y_coords.append(tracked_objects[key][1])
        for j in range(len(x_coords)):
            plt.scatter(x_coords[j],y_coords[j],color = colors[j])
            plt.annotate(j,(x_coords[j],y_coords[j]))
        plt.draw()
        plt.pause(0.00001)
        plt.clf()

        # move detections a bit
        detections = detections + np.random.rand(detections.shape[0],2)*2 -1

        # sometimes add a new detection
        if np.random.rand() > 0.8:
            detections2 = np.random.rand(1,2)*20
            detections = np.concatenate((detections,detections2),0)
        #sometimes delete detections
        if np.random.rand() > 0.8:
            if detections.shape[0] >= 1:
                destroyed = np.random.randint(detections.shape[0])
                # print(tracked_objects[destroyed].id)
                print(tracker.all_objs())
                print('destroyed detection!')

                detections = np.delete(detections,destroyed,0)


        # input updated detections to tracker
        tracked_objects = tracker(detections)
        print(tracked_objects)
        # print(tracker.active_objs[0].get_x(),tracked_objects)
        # for i in tracker.inactive_objs:
        #     print(i.id)
            # for j in i:
            #     print(j.id)
        # print(tracker.inactive_objs)
    # print('Detections Destroyed:' + str(destroyed))
