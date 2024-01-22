using UnityEngine;
using System.Collections;

public class AndroidTouch : MonoBehaviour 
{

	// Use this for initialization
    Transform m_gun;
    public Transform[] m_rocket;
    float m_rocketRate = 0;
    protected int m_rocketchoose = -1;
    public delegate void rocketchoosing(out int i);
    public event rocketchoosing ChooseRocket;
    Vector2 m_screenpos = new Vector2();
	void Start () 
    {
        m_gun = this.transform;
        Input.multiTouchEnabled = true;
	}
	
	// Update is called once per frame
	void MoblieTouch () 
    {
        m_rocketRate -= Time.deltaTime;
        if (Input.touchCount <= 0)
            return;

        if (Input.touchCount == 1)
        {
            switch (Input.touches[0].phase)
            {
                case TouchPhase.Began:
                    {
                        m_screenpos = Input.touches[0].position;
                        break;
                    }
                case TouchPhase.Moved:
                    {
                        m_gun.Translate(new Vector3(Input.touches[0].deltaPosition.x * Time.deltaTime, 0, 0));
                        break;
                    }
            }
            if (Input.touches[0].phase == TouchPhase.Ended || Input.touches[0].phase == TouchPhase.Canceled)
            {
                Vector2 pos = Input.touches[0].position;
                if (m_rocketRate <= 0)
                {
                    m_rocketRate = 0.3f;
                    Instantiate(m_rocket[m_rocketchoose], m_gun.position, m_gun.rotation);
                    ChooseRocket(out m_rocketchoose);
                }
                if (Input.touches[0].phase != TouchPhase.Canceled)
                {
                    if (Mathf.Abs(m_screenpos.x - pos.x) > Mathf.Abs(m_screenpos.y - pos.y))
                    {
                        //左右
                        if (m_screenpos.x > pos.x)
                        {

                        }
                        else
                        {

                        }
                    }
                    else
                    {
                        //上下
                        if (m_screenpos.y > pos.y)
                        {

                        }
                        else
                        {

                        }
                    }
                }
            }
        }
	}
    void Update()
    {
#if !UNITY_EDITOR && (UNITY_iOS || UNITY_ANDROID)
        MoblieTouch();
#endif

    }
}
