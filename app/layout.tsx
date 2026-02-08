import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Academy of Tribes",
  description:
    "Mental health is more than the absence of psychological trauma. Mental health is equally much the growth and resilience of the mind and human experience.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
