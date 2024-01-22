using UnityEngine;
using System.Collections;

public class Enemy2 : MonoBehaviour {

    public Transform m_boss;
    protected Transform m_transform;
    protected GameManager m_GameManager;
    protected Enemy m_enemy;
	// Use this for initialization
	void Start () {

        m_transform = this.transform;
        m_enemy = this.gameObject.GetComponent<Enemy>();
        GameObject obj = GameObject.FindGameObjectWithTag("GameManager");
        if (obj != null)
        {
            m_GameManager = obj.GetComponent<GameManager>();
        }
	}
	
	// Update is called once per frame
	void Update () {

        if (!m_enemy.bossMake)
        {
            if (m_GameManager.Stop)
            {
                Move();
            }
        }
	}

    protected void Move()
    {
        float directX = m_boss.position.x - m_transform.position.x;
        float directY = m_boss.position.y - m_transform.position.y;
        float NextX = m_transform.position.x;
        float NextY = m_transform.position.y;
        float SpeedX;
        float SpeedY;
        float _directX = directX;
        float _directY = directY;
        if (_directX < 0)
        {
            _directX *= -1;
        }
        if (_directY < 0)
        {
            _directY *= -1;
        }
        if (_directX == _directY)
        {
            SpeedX = 5;
            SpeedY = 5;
            if (directX > 0)
            {
                NextX += SpeedX * Time.deltaTime;
                if (NextX > m_boss.position.x)
                {
                    NextX = m_boss.position.x;
                }
            }
            else
            {
                NextX -= SpeedX * Time.deltaTime;
                if (NextX < m_boss.position.x)
                {
                    NextX = m_boss.position.x;
                }
            }
            if (directY > 0)
            {
                NextY += SpeedY * Time.deltaTime;
                if (NextY > m_boss.position.y)
                {
                    NextY = m_boss.position.y;
                }
            }
            else
            {
                NextY -= SpeedY * Time.deltaTime;
                if (NextY < m_boss.position.y)
                {
                    NextY = m_boss.position.y;
                }
            }
        }
        else if (_directX > _directY)
        {
            float x = _directX / 5;
            SpeedY = _directY / x;
            SpeedX = 5;
            if (directX > 0)
            {
                NextX += SpeedX * Time.deltaTime;
                if (NextX > m_boss.position.x)
                {
                    NextX = m_boss.position.x;
                }
            }
            else
            {
                NextX -= SpeedX * Time.deltaTime;
                if (NextX < m_boss.position.x)
                {
                    NextX = m_boss.position.x;
                }
            }
            if (directY > 0)
            {
                NextY += SpeedY * Time.deltaTime;
                if (NextY > m_boss.position.y)
                {
                    NextY = m_boss.position.y;
                }
            }
            else
            {
                NextY -= SpeedY * Time.deltaTime;
                if (NextY < m_boss.position.y)
                {
                    NextY = m_boss.position.y;
                }
            }
        }
        else if (_directX < _directY)
        {
            float x = _directY / 5;
            SpeedX = _directX / x;
            SpeedY = 5;
            if (directX > 0)
            {
                NextX += SpeedX * Time.deltaTime;
                if (NextX > m_boss.position.x)
                {
                    NextX = m_boss.position.x;
                }
            }
            else
            {
                NextX -= SpeedX * Time.deltaTime;
                if (NextX < m_boss.position.x)
                {
                    NextX = m_boss.position.x;
                }
            }
            if (directY > 0)
            {
                NextY += SpeedY * Time.deltaTime;
                if (NextY > m_boss.position.y)
                {
                    NextY = m_boss.position.y;
                }
            }
            else
            {
                NextY -= SpeedY * Time.deltaTime;
                if (NextY < m_boss.position.y)
                {
                    NextY = m_boss.position.y;
                }
            }
        }
        m_transform.position = new Vector3(NextX, NextY, 0);
    }
}
