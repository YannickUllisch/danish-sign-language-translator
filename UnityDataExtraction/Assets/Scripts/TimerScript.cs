using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Events;

public class TimerScript : MonoBehaviour {
    private bool timerIsRunning = false;
    [SerializeField]
    public float totalTime;
    public UnityEvent CountDownEnd;
    private float counter; 


    // Start is called before the first frame update
    public void StartCountdown() {
        timerIsRunning = true; 
        counter = totalTime;
    }

    // Update is called once per frame
    private void Update() {
        if (timerIsRunning) {
            if (counter > 0) {
                counter -= Time.deltaTime;
            } else {
                CountDownEnd.Invoke();
                timerIsRunning = false;
            }
        }
    }
}
