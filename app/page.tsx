import Image from "next/image";

const styles = {
  container: {
    maxWidth: 720,
    margin: "0 auto",
    padding: "60px 24px 80px",
  },
  logoSection: {
    textAlign: "center" as const,
    marginBottom: 48,
  },
  logo: {
    marginBottom: 24,
  },
  h1: {
    fontSize: "1.8rem",
    fontWeight: 400,
    letterSpacing: "0.15em",
    textTransform: "uppercase" as const,
    color: "#1a1a1a",
  },
  tagline: {
    textAlign: "center" as const,
    fontStyle: "italic",
    fontSize: "1.15rem",
    color: "#555",
    marginBottom: 56,
    padding: "0 16px",
    lineHeight: 1.7,
  },
  divider: {
    width: 60,
    height: 1,
    backgroundColor: "#ccc",
    margin: "0 auto 48px",
  },
  author: {
    textAlign: "center" as const,
    fontSize: "0.95rem",
    letterSpacing: "0.05em",
    color: "#777",
    marginBottom: 48,
  },
  paragraph: {
    fontSize: "1.05rem",
    marginBottom: 28,
    textAlign: "left" as const,
    color: "#3a3a3a",
  },
  highlight: {
    fontSize: "1.1rem",
    marginBottom: 28,
    fontStyle: "italic",
    color: "#2c2c2c",
    textAlign: "center" as const,
    padding: "16px 0",
  },
  lastParagraph: {
    fontSize: "1.05rem",
    marginBottom: 0,
    textAlign: "left" as const,
    color: "#3a3a3a",
  },
  footer: {
    textAlign: "center" as const,
    marginTop: 64,
    paddingTop: 32,
    borderTop: "1px solid #e0ddd8",
    fontSize: "0.85rem",
    color: "#999",
    letterSpacing: "0.05em",
  },
};

export default function Home() {
  return (
    <div style={styles.container}>
      <div style={styles.logoSection}>
        <Image
          src="/LogoTHICKV2.png"
          alt="Academy of Tribes Logo"
          width={140}
          height={140}
          style={styles.logo}
          priority
        />
        <h1 style={styles.h1}>Academy of Tribes</h1>
      </div>

      <p style={styles.tagline}>
        Mental health is more than the absence of psychological trauma. Mental
        health is equally much the growth and resilience of the mind and human
        experience.
      </p>

      <div style={styles.author}>Eric Andreas Helsem Schaumburg</div>

      <div style={styles.divider} />

      <div>
        <p style={styles.paragraph}>
          Mental health is more than the absence of psychological trauma. Mental
          health is equally much the growth and resilience of the mind and human
          experience. The modern field of psychology has only existed for a
          little more than 100 years but equivalents and &ldquo;alternative&rdquo;
          practices have existed for millennia. Through religion, philosophy,
          shamanism and many other local/regional cultural institutions. The goal
          has been the same. To understand ourselves and others.
        </p>

        <p style={styles.paragraph}>
          How we understand ourselves and others is ultimately a job for the
          brain. The human brain is in the end an advanced prediction generator.
          It stands to reason that a lot of the unease (and dis-ease) experienced
          in our modern 21st century lives come from an unbalanced match between
          our many prediction models and how we perceive the world. Or to put it
          another way. There is a discrepancy between our predictions of
          ourselves and others, and how we perceive ourselves and others.
        </p>

        <p style={styles.paragraph}>
          Coming back to our cultural institutions and practices that have and
          continue to serve the role of maps and compasses that help us navigate
          our prediction models and perceptions. Depending on who we are, our
          default set of prediction models that organize our personal life and
          our worldview differ. However, our perception of our personal life and
          the world around us might not serve our mental health and well-being.
        </p>

        <p style={styles.highlight}>
          Luckily for all of us there exists an ocean of thoughts and practices
          to help us adjust our perceptions and worldviews.
        </p>

        <p style={styles.lastParagraph}>
          Academy of Tribes seek to help navigate this ocean of thoughts and
          practices to find methods and knowledge that can help this process for
          individuals and businesses alike. To better understand ourselves and
          others in our shared existence.
        </p>
      </div>

      <footer style={styles.footer}>Academy of Tribes</footer>
    </div>
  );
}
