fun onReceive(context: Context, intent: Intent) {
    val forwardIntent = intent.getParcelableExtra<Intent>("next_intent")
    // Trigger: Launching an arbitrary intent provided by another app
    context.startActivity(forwardIntent)
}
