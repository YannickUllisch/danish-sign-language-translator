using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.IO;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using UnityEngine.Events;


public class BasicGestureDetector : MonoBehaviour {
    public GameObject GreenLights;
    public OVRSkeleton leftHandSkeleton;
    public OVRSkeleton rightHandSkeleton;
    private List<OVRBone> leftHandBones;
    private List<OVRBone> rightHandBones;
    private List<string> extractedData;
    private bool isTracking;
    private bool saveFile;
    private int curr_iteration;

    IEnumerator GetFingerBones() {
        do {
            foreach (OVRBone bone in leftHandSkeleton.Bones) {
                leftHandBones.Add(bone);
                //GameObject sphere = GameObject.CreatePrimitive(PrimitiveType.Sphere);
                //sphere.transform.localScale = new Vector3(0.005f, 0.005f, 0.005f);
                //sphere.transform.localPosition = bone.Transform.position;
            } 
            yield return null;
        } while (leftHandSkeleton.Bones.Count <= 0);

        do {
            foreach (OVRBone bone in rightHandSkeleton.Bones) {
                rightHandBones.Add(bone);
                //GameObject sphere = GameObject.CreatePrimitive(PrimitiveType.Sphere);
                //sphere.transform.localScale = new Vector3(0.005f, 0.005f, 0.005f);
                //sphere.transform.localPosition = bone.Transform.position;
            } 
            yield return null;
        } while (rightHandSkeleton.Bones.Count <= 0);
    }

    public void Start() {
        leftHandBones = new List<OVRBone>();
        rightHandBones = new List<OVRBone>();
        StartCoroutine(GetFingerBones());
        curr_iteration = 0;
        saveFile = false;
        isTracking = false;
    }

    void Update() {
        if (isTracking) {
            SpawnGreenLights();
            ExtractData();
        }

        if (saveFile) {
            SaveData(extractedData);
            saveFile = false;
        }

    }

    public void StartTracking() {
        extractedData = new List<string>();
        isTracking = true;
    }

    public void StopTracking() {
        isTracking = false;
        saveFile = true;
    }

    public void ExtractData() {
        List<string> tmpList = new List<string>();
        foreach (OVRBone bone in leftHandBones) {
            //string tmp = (leftHandSkeleton.transform.InverseTransformPoint(bone.Transform.position)).ToString();
            string pos = bone.Transform.position.ToString();
            tmpList.Add(pos);
        }

        foreach (OVRBone bone in rightHandBones) {
            //string tmp = (rightHandSkeleton.transform.TransformPoint(bone.Transform.position)).ToString();
            string pos = bone.Transform.position.ToString();
            tmpList.Add(pos);
        }

        extractedData.Add(string.Join(",", tmpList));
    }

    public void SaveData(List<string> data) {
        string filepath = Application.persistentDataPath + "/" + "soed" + curr_iteration.ToString() + ".csv";
        using (StreamWriter sw = new StreamWriter(filepath)) {
            foreach (string vec in data) {
                sw.WriteLine(vec);
            }
        }
        curr_iteration++;
    }

    public void SpawnSphere(int n) {
        for (int i = 0; i < n; i++) {
            GameObject sphere = GameObject.CreatePrimitive(PrimitiveType.Sphere);
            sphere.transform.localScale = new Vector3(0.5f, 0.5f, 0.5f);
            sphere.transform.localPosition = new Vector3(0, 1, 2);
            sphere.AddComponent<Rigidbody>();
        }
    }

    
    public void SpawnGreenLights() {
        GameObject lights = Instantiate(GreenLights, new Vector3(0.2143418f, 0.0f, 0.7435218f), Quaternion.identity);
        Destroy(lights, 2);
    }
}
