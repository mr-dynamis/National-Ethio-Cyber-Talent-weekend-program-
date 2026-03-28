### 1. Application Layer (Layer 7)
This is where you type and send your message in Telegram.
Telegram app prepares your message (text, emoji, image, etc.).

     Example: You type “Hello” and press send.

### 2. Presentation Layer (Layer 6)
Formats and encrypts the message.
Telegram uses encryption to keep messages secure.

     Your message becomes encoded (so hackers can’t read it).

### 3. Session Layer (Layer 5)
Manages the connection between you and the receiver.
Keeps your chat session active.

    Ensures your conversation stays connected.

### 4. Transport Layer (Layer 4)
Breaks the message into smaller pieces (packets).
Uses protocols like TCP to ensure delivery.

    Makes sure all parts of “Hello” arrive correctly.

### 5. Network Layer (Layer 3)
Adds IP addresses (your device → receiver’s device).
Decides the best path through the internet.

    Like GPS routing your message.

### 6. Data Link Layer (Layer 2)
Converts data into frames.
Uses MAC addresses to move data within the same network.

      Helps transfer data from your Wi-Fi/router.

#### 7. Physical Layer (Layer 1)
Sends raw bits (0s and 1s) through cables, Wi-Fi, or signals.

     Actual transmission via internet signals.

### On the Receiver Side

The process happens in reverse (Layer 1 → Layer 7) until the message appears in their Telegram chat.
