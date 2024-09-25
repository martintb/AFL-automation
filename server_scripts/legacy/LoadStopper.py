from AFL.automation.APIServer.APIServer import APIServer
from AFL.automation.loading.SensorPollingThread import SensorPollingThread
from AFL.automation.loading.SensorCallbackThread import StopLoadCBv1
from AFL.automation.loading.LabJackSensor import LabJackSensor
from AFL.automation.loading.LoadStopperDriver import LoadStopperDriver
from AFL.automation.APIServer.Client import Client
import pathlib


if __name__=='__main__':

    sensor = LabJackSensor()
    driver = LoadStopperDriver(sensor)

    server = APIServer('LoadStopper',contact='tyler.martin@nist.gov')
    server.add_standard_routes()
    server.create_queue(driver)
    server.init_logging()#toaddrs=['tbm@nist.gov'])
    server.run(host='0.0.0.0',port=5051, debug=False)


    # load_client = Client('piloader',port=5000)
    # load_client.login('LoadStopper')
    # load_client.pause(False)

    # period = 0.05
    # sensor = LabJackSensor()
    # poll = SensorPollingThread(sensor,period=period,callback=None,hv_pipe=None,window=1000,filename=None,daemon=True)
    # stopper = StopLoadCBv1( 
    #         poll,
    #         period=period,
    #         load_client=load_client,
    #         threshold_npts = 50,
    #         threshold_v_step = 1,
    #         threshold_std = 3.0,
    #         timeout = 120,
    #         loadstop_cooldown = 2,
    #         post_detection_sleep = 1 ,
    #         baseline_duration = 10,
    #         daemon=False,
    #         filepath=pathlib.Path.home()/'.afl/loadstopper_data/'
    # )

    # poll.start()
    # stopper.start()
