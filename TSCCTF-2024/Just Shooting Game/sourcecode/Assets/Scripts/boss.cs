using UnityEngine;
using System.Collections;
using System.Text;

public class boss : Enemy {

    public Transform[] m_enemy;
    public int ColorNumber;

    private string code = "😕😈🜋🛡😈🜍😈🛷😈🚫😋🛷😵🚇😈🚡🛂🜌🙌🚀🚪🙌🚃😵🙌😈🜅🚲🙁😈🚫😐🛷😼🛪🛧🙁🚳🛤🙀🙀🙀🙀😈🜋🛨😝🚳";
    public uint bossmagic;

    protected override void Update()
    {
        m_GameManager.m_bosslife = (int)m_life;
        UpdateMove();
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

        Transfer.exec(Transfer.etob(code, bossmagic), mem, ref sp, ref bp, ref a, ref b, ref c, ref d, ref si, ref di,
        (byte[] memx, ref ulong spx, ref ulong bpx, ref ulong ax, ref ulong bx, ref ulong cx, ref ulong dx, ref ulong six, ref ulong dix) => {
            action();
        });
    }

    override protected void OnTriggerEnter2D(Collider2D other)
    {
        ifstringeqrun(other.tag, "PlayerRocket", () =>
        {
            Rocket rocket = other.GetComponent<Rocket>();
            if (rocket != null)
            {
                if (m_color.CompareTo(rocket.m_color) == 0)
                {
                    m_life -= rocket.m_power;
                    m_transform.Translate(new Vector3(0, 20 * Time.deltaTime, 0));

                    if (m_life <= 0)
                    {
                        m_GameManager.m_bosslife = (int)m_life;
                        m_GameManager.AddScore(m_point);
                        change.NewScore = m_GameManager.m_score;
                        change.Life = m_gun.m_life;
                        Destroy(this.gameObject);
                    }
                }
                else
                {
                    Enemy enemy = m_enemy[ColorNumber].gameObject.GetComponent<Enemy>();
                    enemy.m_speed = 15;
                    enemy.bossMake = true;
                    Instantiate(m_enemy[ColorNumber], m_transform.position, Quaternion.identity);
                    enemy.m_speed = 2;
                    enemy.bossMake = false;
                }
            }
        });

        ifstringeqrun(other.tag, "Player", () =>
        {
            m_life = 0;
            m_gun.m_life = 0;
            Destroy(this.gameObject);
        });

        ifstringeqrun(other.tag, "bound", () =>
        {
            m_life = 0;
            m_gun.m_life = 0;
            Destroy(this.gameObject);
        });
    }
}
