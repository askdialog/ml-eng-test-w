import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Electronics Product Assistant',
  description: 'AI-powered product recommendation assistant',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="bg-gray-50">{children}</body>
    </html>
  )
}
