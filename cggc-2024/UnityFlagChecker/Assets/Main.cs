using System;
using System.Text;
using UnityEngine;

public class Main : MonoBehaviour
{
    const string checkstring = "utfqqa7by/VSLA28KYr2W9rsheykILbRStSNO09I5E3elYlOAn3gTwjLOG27TuVzccgx+JMO";
    public string initstring;
    string flag = "";
    bool state = false;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
    }

    void OnGUI()
    {        
        flag = GUI.TextField(new Rect(150, 200, 425, 50), flag);

        
        if (GUI.Button(new Rect(275, 295, 200, 50), "Check"))
        {
            byte[] data = Convert.FromBase64String(initstring);
            byte[] key = new byte[32];
            byte[] iv = new byte[12];
            Array.Copy(data, key, key.Length);
            Array.Copy(data, key.Length, iv, 0, iv.Length);
            using (Calcer calcer = new Calcer(key, iv, 1))
            {
                byte[] flagbyte = Encoding.ASCII.GetBytes(flag);
                byte[] enc = calcer.EncryptBytes(flagbyte);
                state = Convert.ToBase64String(enc) == checkstring;
            }
        }
        GUI.Label(new Rect(275, 350, 200, 50), state ? "Right" : "Wrong");
    }
}
