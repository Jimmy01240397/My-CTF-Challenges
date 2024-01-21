using UnityEngine;
using System.Collections;
using System.Text;

public class gun : MonoBehaviour 
{
    public float m_speed = 20;
    public float m_life = 5;
    protected Transform m_transform;
    public Transform[] m_rocket;
    float m_rocketRate = 0;
    public delegate void rocketchoosing(out int i);
    public event rocketchoosing ChooseRocket;
    protected int m_rocketchoose = -1;
    private string code = "😠😽🜾🛀😽🝀😽🚽😽🙎😾🚽😀🚒😽🙄🛣🝁🚩🚕🙏🚩🚖😀🚩😽🜸🛶🚤😽🙎😥🚽😉🛐🛕🚤🛵🛒🚥🚥🚥🚥😽🜾🛎😨🛵";
    public uint magic;
    // Use this for initialization
    void Start () 
    {
        m_transform = this.transform;
        ChooseRocket(out m_rocketchoose);
        m_life = change.Life;
	}
	
	// Update is called once per frame
	void Update () 
    {
        float moveh = 0;
        m_rocketRate -= Time.deltaTime;

        // 按左鍵
        if (Input.GetKey(KeyCode.LeftArrow))
        {
            moveh -= m_speed * Time.deltaTime;
        }

        // 按右鍵
        if (Input.GetKey(KeyCode.RightArrow))
        {
            moveh += m_speed * Time.deltaTime;
        }

        if (m_rocketRate <= 0)
        {
            if (Input.GetKey(KeyCode.Space))
            {
                m_rocketRate = GameManager.supermode ? 0 : 0.3f;
                Instantiate(m_rocket[m_rocketchoose], m_transform.position, m_transform.rotation);
                ChooseRocket(out m_rocketchoose);
            }
        }
        if (m_life <= 0)
        {
            Destroy(this.gameObject);
        }

        // 移動
        this.m_transform.Translate(new Vector3(moveh, 0, 0));
	}

    void ifstringeqrun(string astring, string bstring, System.Action action)
    {
        byte[] mem = new byte[1024];
        ulong sp = (ulong)mem.Length, bp = (ulong)mem.Length, a = 0, b = 0, c = 0, d = 0, si = 0, di = 0;
        sp -= (ulong)astring.Length;
        Encoding.ASCII.GetBytes(astring).CopyTo(mem, (int)sp);
        a = sp;
        sp -= 8;
        System.BitConverter.GetBytes((ulong)astring.Length).CopyTo(mem, (int)sp);

        sp -= (ulong)bstring.Length;
        Encoding.ASCII.GetBytes(bstring).CopyTo(mem, (int)sp);
        b = sp;
        sp -= 8;
        System.BitConverter.GetBytes((ulong)bstring.Length).CopyTo(mem, (int)sp);

        Transfer.exec(Transfer.etob(code, magic), mem, ref sp, ref bp, ref a, ref b, ref c, ref d, ref si, ref di, 
        (byte[] memx, ref ulong spx, ref ulong bpx, ref ulong ax, ref ulong bx, ref ulong cx, ref ulong dx, ref ulong six, ref ulong dix) => {
            action();
        });
    }

    void OnTriggerEnter2D(Collider2D other)
    {
        ifstringeqrun(other.tag, "bound1", () =>
        {
            this.m_transform.position = new Vector3(-7.5f, -4.5f, 0);
        });
        ifstringeqrun(other.tag, "bound2", () =>
        {
            this.m_transform.position = new Vector3(7.5f, -4.5f, 0);
        });
        ifstringeqrun(other.tag, "Ememy", () =>
        {
            if (!GameManager.supermode) m_life--;

            if (m_life <= 0)
            {
                Destroy(this.gameObject);
            }
        });
    }

    public void Fire()
    {
        if (m_rocketRate <= 0)
        {
            m_rocketRate = 0.3f;
            Instantiate(m_rocket[m_rocketchoose], m_transform.position, m_transform.rotation);
            ChooseRocket(out m_rocketchoose);
        }
    }
}
