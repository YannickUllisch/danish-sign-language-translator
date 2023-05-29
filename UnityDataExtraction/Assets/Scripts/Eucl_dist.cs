using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;
using System.Threading;


//[ExecuteInEditMode]
public class Eucl_dist : MonoBehaviour {

    public GameObject Righthand;
    public float distance_float;
    public float distance_away;
    private float distanceBetweenObjects;
    public UnityEvent buttonPressed;
    private bool isActive;

    private void Start(){
        isActive = false;
    }
    private void Update() {
        distanceBetweenObjects = Vector3.Distance(transform.position, Righthand.transform.position);
        Debug.DrawLine(transform.position, Righthand.transform.position, Color.red);

        if(distanceBetweenObjects <= distance_float) {
            isActive = true;
        }

        EuclidAlg(distanceBetweenObjects);
    }

    private void EuclidAlg(float dist) {
        if (isActive && (dist > distance_away)) {
            buttonPressed.Invoke();
            isActive = false;
        }
    }

    public void StartCountdown() {

    }

    public void SpawnSphere() {
        GameObject sphere = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        sphere.transform.localScale = new Vector3(0.3f, 0.3f, 0.3f);
        sphere.transform.localPosition = new Vector3(0, 1, 2);
        sphere.AddComponent<Rigidbody>();
    }
}
